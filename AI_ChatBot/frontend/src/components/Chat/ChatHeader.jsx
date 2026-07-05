import React from "react";

const ChatHeader = ({ totalFiles }) => {
  return (
    <div className="border-b border-zinc-800 p-5">

      <h1 className="text-2xl font-bold">
        🤖 RAG Assistant
      </h1>

      <p className="text-zinc-400 text-sm mt-1">
        {totalFiles} PDF{totalFiles !== 1 ? "s" : ""} Uploaded
      </p>

    </div>
  );
};

export default ChatHeader;