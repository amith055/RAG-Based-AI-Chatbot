import React from "react";
import ChatMessage from "./ChatMessage";

const ChatMessages = ({ messages }) => {
  return (
    <div className="flex-1 overflow-y-auto p-6 space-y-6">

      {messages.map((message, index) => (
        <ChatMessage
          key={index}
          message={message}
        />
      ))}

    </div>
  );
};

export default ChatMessages;