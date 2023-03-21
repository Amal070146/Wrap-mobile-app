import React from "react";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios"

const Login = () => {
  const navigate = useNavigate();
  const [password, setpassword] = useState();
  const [email, setemail] = useState();
  const history = useNavigate();
  const handle = () => {
    axios.post("http://localhost:3001/login", {
      Email: email,
      Pass: password,
    }).then((response)=>{
      console.log(response)
    })

  };
  return (
    <div className="signin-wrapper">
      <div className="signin-wrapper-image">
        <h2>Welcome Back </h2>
      </div>
      <div className="form-signin-wrapper">
        <form action="">
          <div className="form-signin">
            <label htmlFor="">Email :</label>
            <input
              type="text"
              id="fname"
              name="name"
              placeholder="Your Email.."
              onChange={(e) => setemail(e.target.value)}
            />
          </div>

          <div className="form-signin">
            <label htmlFor="">Password :</label>
            <input
              type="password"
              id="fname"
              name="name"
              placeholder="Enter Password"
              onChange={(e) => setpassword(e.target.value)}
            />
          </div>

          <div className="submitbutton">
            <button onClick={handle}>Submit</button>
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
