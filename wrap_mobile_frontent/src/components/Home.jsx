import React, { useEffect, useState } from "react";
import axios from "axios";

function Home() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const checkLoginStatus = async () => {
      try {
        const response = await axios.get("/api/check-auth/");
        if (response.status === 200) {
          setIsLoggedIn(true);
        }
      } catch (error) {
        console.log(error.response.data);
      }
    };
    checkLoginStatus();
  }, []);

  return (
    <div>
      <h2>Home</h2>
      {isLoggedIn ? (
        <p>You are logged in!</p>
      ) : (
        <p>Please log in to view this page.</p>
      )}
    </div>
  );
}

export default Home;
