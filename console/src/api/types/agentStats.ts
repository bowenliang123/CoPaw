export interface ChannelStats {
  channel: string;
  user_messages: number;
  assistant_messages: number;
  total_messages: number;
}

export interface DailyStats {
  date: string;
  chats: number;
  active_sessions: number;
  user_messages: number;
  assistant_messages: number;
  total_messages: number;
  unique_users: number;
}

export interface AgentStatsSummary {
  total_active_sessions: number;
  total_messages: number;
  total_user_messages: number;
  total_assistant_messages: number;
  by_date: DailyStats[];
  channel_stats: ChannelStats[];
  start_date: string;
  end_date: string;
}
