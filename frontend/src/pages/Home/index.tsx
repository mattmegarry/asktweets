import React, { useState } from "react";
import MPSelect from "../../components/MPSelect";

import config from "../../config";
const { baseUrl } = config;

const Home = () => {
  const [selectedMp, setSelectedMp] = useState(null);
  const [llmResponse, setLlmResponse] = useState("");

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    console.log(process.env.NODE_ENV);
    if (!selectedMp) return;
    const { id: mpId } = selectedMp;
    const response = await fetch(`${baseUrl}/prompt/${mpId}`, {
      method: "POST",
    });
    const data = await response.json();
    setLlmResponse(data);
  };

  return (
    <>
      <h1>Home</h1>
      <p>Select and MP from the dropdown below to see query the API</p>
      <form onSubmit={handleSubmit}>
        <MPSelect setSelectedMp={setSelectedMp} />

        <button type="submit">Submit</button>
      </form>
      <div className="llm-response">
        <p>{llmResponse}</p>
      </div>
    </>
  );
};

export default Home;
