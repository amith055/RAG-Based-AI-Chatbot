import React from "react";
import { Bot, User } from "lucide-react";

const ChatMessage = ({ message }) => {
  const isUser = message.type === "user";

  return (
    <div
      className={`flex ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`max-w-3xl rounded-2xl px-5 py-4 ${
          isUser
            ? "bg-blue-600 text-white"
            : "bg-zinc-900 text-white"
        }`}
      >
        <div className="flex items-start gap-3">

          {isUser ? (
            <User size={20} />
          ) : (
            <Bot size={20} />
          )}

          <p className="leading-relaxed whitespace-pre-wrap">
            {message.text}
          </p>

        </div>
      </div>
    </div>
  );
};

export default ChatMessage;