import React from "react";
import { Loader2 } from "lucide-react";

const Loader = () => {
  return (
    <div className="flex items-center justify-center p-5">
      <Loader2
        size={28}
        className="animate-spin text-blue-500"
      />
    </div>
  );
};

export default Loader;