import React, { useState, useEffect } from "react";
import "./KnowledgeBase.css";

function KnowledgeBase() {
  const [data, setData] = useState([]);
  const [query, setQuery] = useState("");
  const [filteredData, setFilteredData] = useState([]);

  useEffect(() => {
    fetch("/updated_knowledge_base.json")
      .then((response) => response.json())
      .then((data) => {
        setData(data);
        setFilteredData(data);
      });
  }, []);

  const handleSearch = (event) => {
    const value = event.target.value;
    setQuery(value);
    const filtered = data.filter((item) =>
      item.question.toLowerCase().includes(value.toLowerCase())
    );
    setFilteredData(filtered);
  };

  return (
    <div className="base">
      <h2>База знаний</h2>
      <input
        type="text"
        placeholder="Поиск по названиям..."
        value={query}
        onChange={handleSearch}
        className="search-input"
      />
      <div className="base-container">
        <ul className="knowledge-list">
          {filteredData.map((item) => (
            <li key={item.id} className="knowledge-item">
              <a
                href={item.filename}
                target="_blank"
                rel="noopener noreferrer"
                className="knowledge-link"
              >
                {item.question}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default KnowledgeBase;
