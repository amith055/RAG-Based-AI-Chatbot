import React from "react";
import UploadButton from "./UploadButton";
import UploadedFile from "./UploadedFile";

const Sidebar = ({ files, onUpload }) => {
  return (
    <div className="w-80 bg-zinc-950 border-r border-zinc-800 flex flex-col p-5">

      <h1 className="text-2xl font-bold mb-6">
        📄 Documents
      </h1>

      <UploadButton onUpload={onUpload} />

      <div className="mt-8 flex-1 overflow-y-auto">

        <h2 className="text-lg font-semibold mb-4">
          Uploaded PDFs
        </h2>

        {files.length === 0 ? (
          <p className="text-zinc-500">
            No PDF uploaded
          </p>
        ) : (
          <div className="space-y-3">

            {files.map((file, index) => (
              <UploadedFile
                key={index}
                file={file}
              />
            ))}

          </div>
        )}

      </div>

    </div>
  );
};

export default Sidebar;