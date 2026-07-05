import React, { useState } from "react";
import api from "../services/api";
import Sidebar from "../components/Sidebar/Sidebar";
import ChatHeader from "../components/Chat/ChatHeader";
import ChatMessages from "../components/Chat/ChatMessages";
import ChatInput from "../components/Chat/ChatInput";
import TypingIndicator from "../components/Chat/TypingIndicator";

const Chat = () => {
  const [files, setFiles] = useState([]);

  const [messages, setMessages] = useState([
    {
      type: "bot",
      text: "👋 Welcome! Upload one or more PDFs and ask me anything about them.",
    },
  ]);

  const [loading, setLoading] = useState(false);

  const handleUpload = async (uploadedFiles) => {

    setFiles((prev) => [...prev, ...uploadedFiles]);

    const formData = new FormData();

    uploadedFiles.forEach((file) => {
        formData.append("files", file);
    });

    try {

        const response = await api.post(
            "/upload",
            formData,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            }
        );

        console.log(response.data);

    } catch (error) {
        console.log(error);
    }
};

  const handleSend = (text) => {
    setMessages((prev) => [
      ...prev,
      {
        type: "user",
        text,
      },
    ]);

    setLoading(true);

    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          type: "bot",
          text: "Your RAG backend response will appear here.",
        },
      ]);

      setLoading(false);
    }, 1500);
  };

  return (
    <div className="h-screen bg-[#0f172a] text-white flex overflow-hidden">

      {/* Sidebar */}

      <div className="w-[320px] border-r border-slate-700 bg-[#111827] shadow-xl">
        <Sidebar
          files={files}
          onUpload={handleUpload}
        />
      </div>

      {/* Main Chat */}

      <div className="flex flex-col flex-1">

        {/* Header */}

        <div className="backdrop-blur-md border-b border-slate-700 bg-[#111827]/70">
          <ChatHeader totalFiles={files.length} />
        </div>

        {/* Chat */}

        <div className="flex-1 overflow-hidden bg-gradient-to-b from-[#0f172a] to-[#111827]">

          <div className="h-full max-w-5xl mx-auto flex flex-col">

            <div className="flex-1 overflow-y-auto px-8 py-8">

              <ChatMessages
                messages={messages}
              />

              {loading && (
                <div className="mt-6">
                  <TypingIndicator />
                </div>
              )}

            </div>

            {/* Input */}

            <div className="sticky bottom-0 bg-gradient-to-t from-[#111827] via-[#111827] to-transparent pt-6 pb-8">

              <div className="max-w-4xl mx-auto">

                <ChatInput
                  onSend={handleSend}
                />

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
};

export default Chat;