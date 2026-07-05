import React, { useState } from "react";
import { Send } from "lucide-react";

const ChatInput = ({ onSend }) => {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    if (!message.trim()) return;

    onSend(message);
    setMessage("");
  };

  return (
    <div className="border-t border-zinc-800 p-5">
      <div className="flex gap-3">

        <input
          type="text"
          className="flex-1 bg-zinc-900 rounded-xl px-5 py-3 outline-none text-white"
          placeholder="Ask something about your PDFs..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") handleSend();
          }}
        />

        <button
          onClick={handleSend}
          className="bg-blue-600 hover:bg-blue-700 rounded-xl px-5 flex items-center justify-center"
        >
          <Send size={20} />
        </button>

      </div>
    </div>
  );
};

export default ChatInput;