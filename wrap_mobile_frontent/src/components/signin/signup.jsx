import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Signup = () => {
  const [name, setname] = useState();
  const [password, setpassword] = useState();
  const [email, setemail] = useState();
  const history = useNavigate();
  const handle = () => {
    axios.post("http://localhost:3001/signin", {
      Name: name,
      Email: email,
      Pass: password,
    });

    history("/profile");
  };

  return (
    <div className="signin-wrapper">
      <div className="signin-wrapper-image">
        <h2>Welcome to Tetra</h2>
      </div>
      <div className="form-signin-wrapper">
        <form action="/loginresponse">
          <div className="form-signin">
            <label htmlFor="">Name :</label>
            <input
              type="text"
              id="fname"
              name="name"
              placeholder="Your name.."
              onChange={(e) => setname(e.target.value)}
            />
          </div>
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
              onChange={(e) => setpassword(e.target.value)}
            />
          </div>
          <div className="form-signin">
            <label htmlFor="">Confirm Password :</label>
            <input
              type="password"
              id="fname"
              name="name"
              placeholder="Confirm password..."
            />
          </div>
          <div className="submitbutton">
            <button
              // onClick={(e) => {
              //   navigate("/profile");
              // }}
              onClick={handle}
            >
              Submit
            </button>
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
