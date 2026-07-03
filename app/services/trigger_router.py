class TriggerRouter:

    def get_prompt_type(self, trigger_kind: str) -> str:

        research = {
            "research_digest",
            "category_research_digest_release",
            "regulation_change",
        }

        performance = {
            "perf_spike",
            "perf_dip",
            "milestone_reached",
            "review_theme_emerged",
        }

        marketing = {
            "festival_upcoming",
            "weather_heatwave",
            "local_news_event",
            "category_trend_movement",
            "competitor_opened",
        }

        customer = {
            "customer_lapsed_soft",
            "appointment_tomorrow",
            "recall_due",
        }

        engagement = {
            "dormant_with_vera",
            "scheduled_recurring",
        }

        if trigger_kind in research:
            return "research"

        if trigger_kind in performance:
            return "performance"

        if trigger_kind in marketing:
            return "marketing"

        if trigger_kind in customer:
            return "customer"

        if trigger_kind in engagement:
            return "engagement"

        return "generic"