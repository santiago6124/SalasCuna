import React, { useState } from "react";
import "./SearchBar.css";
import SearchIcon from "@mui/icons-material/Search";
//import CloseIcon from "@material-ui/icons/Close";

const SearchBar = ({ keyword, placeholder, onChange }) => {
  

    return (
        <div className="search">
          <div className="searchInputs">
            <input className="SearchBar" key="search-bar" placeholder={placeholder} 
                value={keyword} onChange={(e) => onChange(e.target.value)}
            />
            <div className="searchIcon">
              <SearchIcon/>
            </div>
          </div>
        </div>
    );
}

export default SearchBar;