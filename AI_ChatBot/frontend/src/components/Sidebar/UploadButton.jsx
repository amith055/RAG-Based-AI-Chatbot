import React, { useRef } from "react";
import { Upload } from "lucide-react";

const UploadButton = ({ onUpload }) => {
  const fileInputRef = useRef(null);

  const handleUpload = (e) => {
    const uploadedFiles = Array.from(e.target.files);

    if (uploadedFiles.length > 0) {
      onUpload(uploadedFiles);
    }
  };

  return (
    <>
      <button
        onClick={() => fileInputRef.current.click()}
        className="bg-blue-600 hover:bg-blue-700 rounded-xl p-3 w-full flex items-center justify-center gap-2"
      >
        <Upload size={18} />
        Upload PDF
      </button>

      <input
        ref={fileInputRef}
        type="file"
        multiple
        accept=".pdf"
        hidden
        onChange={handleUpload}
      />
    </>
  );
};

export default UploadButton;