import React from "react";
import { FileText, Trash2 } from "lucide-react";

const UploadedFile = ({ file }) => {
  return (
    <div className="bg-zinc-900 rounded-xl p-3 flex items-center justify-between">

      <div className="flex items-center gap-3 overflow-hidden">

        <FileText
          size={18}
          className="text-red-500"
        />

        <span className="truncate text-sm">
          {file.name}
        </span>

      </div>

      <Trash2
        size={16}
        className="text-zinc-500 hover:text-red-500 cursor-pointer"
      />

    </div>
  );
};

export default UploadedFile;