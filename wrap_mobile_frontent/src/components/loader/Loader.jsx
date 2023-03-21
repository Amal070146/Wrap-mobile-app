import React, { useState, useEffect } from "react";
import { Navigate } from "react-router-dom";

const Loader = () => {
  const [redirect, setRedirect] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setRedirect(true);
    }, 2000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="loader">
      <h1>Loading...</h1>
      {redirect && <Navigate to="/login" />}
    </div>
  );
};

export default Loader;
