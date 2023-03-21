import React from "react";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios"

const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const [email, setEmail] = useState();
  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/api/login/", {
        username,
        email,
        password,
      });
      console.log(response);
      // if (response.status === 200) {
      //   // redirect to home page after successful login
      //   navigate("/");
      // }
    } catch (error) {
      setError(error.response.data.error);
    }
  };
  return (
    <div className="signin-wrapper">
      <div className="signin-wrapper-image">
        <h2>Welcome Back </h2>
      </div>
      <div className="form-signin-wrapper">
        {error && <p className="text-danger">{error}</p>}
        <form onSubmit={handleLogin}>
          <div className="form-group">
            <label>Username:</label>
            <input
              type="text"
              name="username"
              className="form-control"
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className="form-signin">
            <label>Email :</label>
            <input
              type="text"
              id="fname"
              name="email"
              placeholder="Your Email.."
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <div className="form-group">
            <label>Password:</label>
            <input
              type="password"
              className="form-control"
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <div className="submitbutton">
            {/* <button onClick={handleLogin}>Submit</button> */}
            <a href="" onClick={(e) => navigate("/dashboard")}>Submit</a>
          </div>
        </form>
      </div>
      <div className="login-here">
        <p>Don’t have an account?</p>
        <span>
          <a href="" onClick={(e) => navigate("/signup")}>
            Register now
          </a>
        </span>
      </div>
      <div></div>
      <div></div>
    </div>
  );
};

export default Login;
