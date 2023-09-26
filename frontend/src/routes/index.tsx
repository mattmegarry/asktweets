import React from "react";
import { Routes, Route } from "react-router-dom";

import Layout from "../components/Layout";

import Home from "../pages/Home";

const Router = () => {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="*" element={<h2>Not Found</h2>} />
      </Route>
    </Routes>
  );
};

export default Router;
