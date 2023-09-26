import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header>
      <div className="wrap">
        <div className="header-content">
          <h1>Ask MP Tweets</h1>
          <nav>
            <div className="header-nav-item">
              <Link className="header-nav-anchor" to="explainer">
                Explainer
              </Link>
            </div>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;
