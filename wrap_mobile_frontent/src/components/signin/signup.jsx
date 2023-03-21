import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Signup = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password1, setPassword1] = useState("");
  const [password2, setPassword2] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();
  const handleSignup = async (e) => {
    e.preventDefault();
    if (password1 !== password2) {
      setError("Passwords do not match");
      return;
    }
    try {
      const response = await axios.post("http://localhost:8000/api/signup/", {
        username,
        email,
        password1,
        password2,
      });
      if (response.status === 201) {
        // redirect to home page after successful signup
        navigate("/profile", { replace: true });
      }
    } catch (error) {
      setError(error.response.data.error);
    }
  };

  return (
    <div className="signin-wrapper">
      <div className="signin-wrapper-image">
        <h2>Welcome to Wrap</h2>
      </div>
      <div className="form-signin-wrapper">
        {error && <p className="text-danger">{error}</p>}
        <form onSubmit={handleSignup}>
          <div className="form-signin">
            <label htmlFor="">Name :</label>
            <input
              type="text"
              id="fname"
              name="name"
              placeholder="Your name.."
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
          <div className="form-signin">
            <label htmlFor="">Age : </label>
            <input
              type="text"
              id="fname"
              name="name"
              placeholder="Your Age.."
            />
          </div>
          <div className="form-signin">
            <label htmlFor="">Phone :</label>
            <input
              type="number"
              id="fname"
              name="name"
              placeholder="Your phone number.."
            />
          </div>
          <div className="form-signin">
            <label htmlFor="">Password :</label>
            <input
              type="password"
              id="fname"
              name="name"
              placeholder="Enter Password"
              onChange={(e) => setPassword1(e.target.value)}
            />
          </div>
          <div className="form-signin">
            <label htmlFor="">Confirm Password :</label>
            <input
              type="password"
              id="fname"
              name="name"
              placeholder="Confirm password..."
              onChange={(e) => setPassword2(e.target.value)}
            />
          </div>
          <div className="submitbutton">
            {/* <button
              // onClick={(e) => {
              //   navigate("/profile");
              // }}
              onClick={handleSignup}
            >
              Submit
            </button> */}
            <a href="" onClick={(e) => navigate("/dashboard")}>Submit</a>
          </div>
        </form>
      </div>
      <div className="login-here">
        <p>Already have an account?</p>
        <span>
          <a href="./login">Login Here</a>
        </span>
      </div>
      <div></div>
      <div></div>
    </div>
  );
};

export default Signup;
