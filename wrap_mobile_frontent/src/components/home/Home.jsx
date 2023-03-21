import React from "react";
import "./home.css";
import { BiDownArrow } from "react-icons/bi";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();
  return (
    <div className="home">
      <div class="container">
        <div class="row">
          <div class="">
            <h3 class="animate-charcter"> WRAP</h3>
          </div>
        </div>
        <div>
          <BiDownArrow
            className="scroll_down"
            onClick={(e) => {
              navigate("/login");
            }}
          />
        </div>
      </div>
    </div>
  );
};

export default Home;
