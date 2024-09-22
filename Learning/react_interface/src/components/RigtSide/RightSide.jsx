import React from "react";
import CustomerReview from "../CustomerReview/CustomerReview";
import Updates from "../Updates/Updates";
import "./RightSide.css";

const RightSide = () => {
  return (
    <div className="RightSide">
      <div>
        <h3>Recent Updates</h3>
        <Updates />
      </div>
      <div>
        <h3>Energy Rate</h3>
        <CustomerReview />
      </div>
    </div>
  );
};

export default RightSide;
