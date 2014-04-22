"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class IEventsManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IEventsManagement
    """

    def getAllAgentAlerts(self, agentId):
        """Gets the summary information for all alerts
        associated with the specified agent. Note that this list can
        potentially be very large.
        """
        return self.session.request('events/agents/%s/alerts/all'
                % (agentId))

    def getAgentAlertsByPage(self, agentId, page):
        """Gets summary info for alerts for a given agent ID,
        such that the results are paged for easy viewing in a paged
        grid.
        """
        return self.session.request('events/agents/%s/alerts/paged?max=%s&page=%s'
                % (agentId, page))

    def getAgentAlertsCount(self, agentId):
        """Gets non-dismissed alerts count for specified
        agent.
        """
        return self.session.request('events/agents/%s/alertsCount'
                % (agentId))

    def getAllAgentEvents(self, agentId):
        """Gets the summary information for all events
        associated with the specified agent. Note that this list can
        potentially be very large.
        """
        return self.session.request('events/agents/%s/all'
                % (agentId))

    def dismissAllAgentAlerts(self, agentId):
        """Marks all alerts for the agent as read, thereby
        dismissing them from the list of alerts.
        """
        return self.session.request('events/agents/%s/all'
                % (agentId), 'DELETE')

    def getAgentEventsCount(self, agentId):
        """Gets events count for specified agent."""
        return self.session.request('events/agents/%s/eventsCount'
                % (agentId))

    def getAgentEventsByPage(self, agentId, page):
        """Gets summary info for events for a given agent ID,
        such that the results are paged for easy viewing in a paged
        grid.
        """
        return self.session.request('events/agents/%s/paged?max=%s&page=%s'
                % (agentId, page))

    def getCachedEventsByDate(self, data):
        """Gets the summary information for cached events
        associated with the specified core ordering by date.
        """
        return self.session.request('events/cachedEventsDateParam', 'PUT',
                    self.getXML(data, 'EventsDateRange'))

    def getConfiguration(self):
        """Returns configuration information for events such
        as email content and notification settings.
        """
        return self.session.request('events/config')

    def setConfiguration(self, data):
        """Sets configuration information for events such as
        email content and notification settings.
        """
        return self.session.request('events/config', 'PUT',
                    self.getXML(data, 'eventsConfiguration'))

    def getAgentAlertsSettings(self, agentId):
        """Returns the alert settings for the specified agent
        such as email content and notification settings.
        """
        return self.session.request('events/config/agents/%s'
                % (agentId))

    def setAgentAlertsSettings(self, data, agentId):
        """Sets alert settings for the specified agent such
        as email content and notification settings.
        """
        return self.session.request('events/config/agents/%s'
                % (agentId), 'PUT',
                    self.getXML(data, 'agentAlertSettings'))

    def sendTestEmail(self, data):
        """Generates and sends a test email notification
        based on the specified email configuration.
        """
        return self.session.request('events/config/email/test', 'PUT',
                    self.getXML(data, 'sendTestEmailRequest'))

    def getAllCoreAlerts(self):
        """Gets the summary information for all alerts
        associated with the core. Note that this list can
        potentially be very large.
        """
        return self.session.request('events/core/alerts/all')

    def getCoreAlertsByPage(self, page):
        """Gets summary info for events for the core, such
        that the results are paged for easy viewing in a paged grid.
        """
        return self.session.request('events/core/alerts/paged?max=%s&page=%s'
                % (page))

    def getCoreAlertsCount(self):
        """Gets non-dismissed alerts count for core."""
        return self.session.request('events/core/alertsCount')

    def getAllCoreEvents(self):
        """Gets the summary information for all events
        associated with the core. Note that this list can
        potentially be very large.
        """
        return self.session.request('events/core/all')

    def dismissAllCoreAlerts(self):
        """Marks all alerts for the core as read, thereby
        dismissing them from the list of alerts.
        """
        return self.session.request('events/core/all', 'DELETE')

    def getCoreEventsCount(self):
        """Gets events count for core."""
        return self.session.request('events/core/eventsCount')

    def getCoreEventsByPage(self, page):
        """Gets summary info for events for the core, such
        that the results are paged for easy viewing in a paged grid.
        """
        return self.session.request('events/core/paged?max=%s&page=%s'
                % (page))

    def getDetailsForEvent(self, eventId):
        """Gets the details for a single event."""
        return self.session.request('events/event/%s'
                % (eventId))

    def dismissEvent(self, eventId):
        """Marks an event as read, thereby dismissing it from
        the list of events.
        """
        return self.session.request('events/event/%s'
                % (eventId), 'DELETE')

    def getEventsByDate(self, data):
        """Gets the summary information for all events
        associated with the specified core ordering by date.
        """
        return self.session.request('events/EventsDateRange', 'PUT',
                    self.getXML(data, 'EventsDateRange'))

    def getEventTypes(self):
        """Gets the list of all possible event types,
        organized into groups.
        """
        return self.session.request('events/types')
