import React, { useEffect, useState } from "react";
import Select from "react-select";

import config from "../../config";
const { baseUrl } = config;

const options = [
  { value: "chocolate", label: "Chocolate" },
  { value: "strawberry", label: "Strawberry" },
  { value: "vanilla", label: "Vanilla" },
];

const MPSelect = ({ setSelectedMp }: any) => {
  const [mps, setMps] = useState([]);

  useEffect(() => {
    const getMps = async () => {
      fetch(`${baseUrl}/mps`)
        .then((res) => res.json())
        .then((data) => {
          setMps(data);
        });
    };
    getMps();
  }, []);

  function handleChange(option: any) {
    setSelectedMp(option);
  }

  return (
    <>
      <Select options={mps} onChange={handleChange} />
    </>
  );
};

export default MPSelect;
