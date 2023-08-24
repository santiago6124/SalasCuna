import React, { useState, useEffect } from "react";

const SearchComponent = () => {

  const [chico, setChico] = useState([]);
  const [search, setSearch] = useState("");

  const URL = "http://127.0.0.1:8000/api/child/";

  const showData = async () => {
    const response = await fetch(URL);
    const data = await response.json();
    //console.log(data)
    setChico(data);
  };
  //función de búsqueda
  const searcher = (e) => {
    setSearch(e.target.value);
  };

  const results = !search
    ? chico
    : chico.filter((dato) =>
        dato.name.toLowerCase().includes(search.toLocaleLowerCase())
      );

  useEffect(() => {
    showData();
  }, []);

  //renderizamos la vista
  return (
    <div>
      <input
        value={search}
        onChange={searcher}
        type="text"
        placeholder="Search"
        className="form-control"
      />
      <table className="table table-striped table-hover mt-5 shadow-lg">
        <thead>
          <tr className="bg-curso text-white">
            <th>Nombre</th>
            <th>Apellido</th>
          </tr>
        </thead>
        <tbody>
          {results.map((user) => (
            <tr key={user.id}>
              <td>{chico.name}</td>
              <td>{chico.apellido}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
export default SearchComponent;
