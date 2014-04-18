#!/bin/bash
# autoImplementInterface.sh
# Download AppAssure docs and create Python classes.

URL="http://docs.appassure.com/display/AA50D/"
newline=$'\n'

[[ -x $(which html2text 2>/dev/null) ]] || (
        echo "You must have html2text installed."
        exit 1
        ) || exit 1

babyCamel() {
    # Convert a string from CamelCase to babyCamelCase.
    echo "$(tr [A-Z] [a-z] <<< ${1::1})${1:1}"
}

getData() {
    echo "$(wget -q -O- "${1}" |
            html2text -ascii -nobs |
            grep -v Child_Pages |
            sed 's/\*\*\*\*\*$//g' |
            awk '/\*\*\*\*\*/,/HTTP Method: /' |
            sed 's/[^*]\*[^*]//; s/\*\*\*\*\* /*/g')"
}

read -p "Interface name: " interface
echo "Downloading and parsing AppAssure docs..."
interface_url="${URL}${interface}"
data="$(getData "$interface_url")"

if [[ -z $data ]]; then
    echo "Failed. Bad interface name?"
    echo "Some pages in the AppAssure docs follow a different format."
    echo "If you'd like, you can enter the URL manually, and we'll try again."
    read -p "Continue? [y/N]: " ans
    [[ $ans == y || $ans == Y ]] || exit
    read -p "URL: " interface_url
    data="$(getData "$interface_url")"
    if [[ -z $data ]]; then
        echo "Failed again. Giving up this time."
        exit 1
    fi
fi

echo "Creating new Python script ${interface}.py"
cat << EOF > ${interface}.py
"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class ${interface}(AppAssureAPI):
    """Full documentation online at
    ${interface_url}
    """

EOF

IFS='*'
for section in ${data}; do
    function="$(head -1 <<< "${section}" | sed 's/\s*$//g')"
    uri="$(grep '^URI: ' <<< "${section}" | sed 's/^URI: //g;')"
    method="$(grep '^HTTP Method: ' <<< ${section} | sed 's/^.*Method://g; s/ //g')"
    summary=""
    summaryTemp=""
    uriVars=( )
    arguments="self"

    # If the function is blank, get out fast
    [[ -z ${function} ]] && continue

    # Parse out and prettify the summary.
    IFS=$'\n'
    for line in $(grep -vP "^(URI: |HTTP Method: |${function})" <<< "${section}"); do
        summary="${summary} ${line}"
    done
    summary="$(fold -s -w65 <<< "${summary}")"
    for line in ${summary}; do
        summaryTemp="${summaryTemp}        ${line}${newline}"
    done
    summary="$(sed 's/          *Summary: //' <<< "${summaryTemp}")"
    if ! [[ ${summary: -1} == . ]]; then
        summary="${summary}."
    fi
    IFS='*'

    # Translate our URI into the format expected by Python.
    if (grep -q "{" <<< "${uri}"); then
        pyuri="$(sed 's/{[^{]*}/%s/g' <<< "${uri}")"
        if (grep -q '%s' <<< "${pyuri}"); then
            IFS='/'
            for field in ${uri}; do
                uriVars+=("$(grep '{.*}' <<< "${field}" |
                    sed 's/[{}]//g; s/.*=//g')")
            done
            IFS='*'
        fi
        pyuri="'${pyuri}'
                % ("
        for var in ${uriVars[@]}; do
            [[ -n ${var} ]] && pyuri="${pyuri}${var}, "
        done
        pyuri="$(sed 's/, )/)/g' <<< "${pyuri})")"

    else
        pyuri="'${uri}'"
    fi

    # Formulate the final request string and determine function args.
    if [[ ${method} != GET && ${method} != DELETE ]]; then
        # This part can't be automated easily, you'll have to copy this
        # info from the docs.
        echo -n "XML tag for ${function} (blank for no request body): "
        read tag
        if [[ -z $tag ]]; then
            request="${pyuri}, '${method}'"
        else
            request="${pyuri}, '${method}',
                    self.getXML(data, '${tag}')"
            arguments="$arguments, data"
        fi
    else
        request="${pyuri}"
    fi
    # Add the other args, if they exist
    if [[ -n ${uriVars[@]} ]]; then
        for var in ${uriVars[@]}; do
            [[ -n ${var} ]] && arguments="${arguments}, ${var}"
        done
    fi

    # Write the function to the file.
    cat << EOF >> ${interface}.py
    def $(babyCamel ${function})(${arguments}):
EOF
    if [[ $(wc -c <<< ${summary}) -lt 65 ]]; then
        cat << EOF >> ${interface}.py
        """${summary}"""
EOF
    else
        cat << EOF >> ${interface}.py
        """${summary}
        """
EOF
    fi
    cat << EOF >> ${interface}.py
        return self.session.request(${request})

EOF
done

# Clean up the file.
sed -i '$ d; s/ *$//' "${interface}.py"
