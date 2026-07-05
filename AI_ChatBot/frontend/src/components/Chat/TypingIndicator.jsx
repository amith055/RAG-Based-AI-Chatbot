import React from "react";
import { Loader2 } from "lucide-react";

const TypingIndicator = () => {
  return (
    <div className="flex justify-start px-6 pb-4">

      <div className="bg-zinc-900 rounded-2xl px-5 py-4 flex items-center gap-3">

        <Loader2
          size={20}
          className="animate-spin"
        />

        <span>Thinking...</span>

      </div>

    </div>
  );
};

export default TypingIndicator;