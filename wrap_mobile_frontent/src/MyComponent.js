import React, { useState, useEffect } from "react";
import axios from "axios";

function MyComponent() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await axios.get("/api/mymodels/");
      setData(response.data);
    }
    fetchData();
  }, []);

  return (
    <div>
      <h1>My Models</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>
            {item.name}:{item.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MyComponent;
