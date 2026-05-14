# -*- coding: utf-8 -*-
"""Agent statistics models."""

from __future__ import annotations

from pydantic import BaseModel


class ChannelStats(BaseModel):
    channel: str
    session_count: int
    user_messages: int
    assistant_messages: int
    total_messages: int


class DailyStats(BaseModel):
    date: str
    chats: int
    active_sessions: int
    user_messages: int
    assistant_messages: int
    total_messages: int
    unique_users: int


class AgentStatsSummary(BaseModel):
    total_active_sessions: int
    total_messages: int
    total_user_messages: int
    total_assistant_messages: int
    by_date: list[DailyStats]
    channel_stats: list[ChannelStats]
    start_date: str
    end_date: str
