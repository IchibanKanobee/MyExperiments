// WorldMap.js
import React from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";

// GeoJSON URL (replace with your own if necessary)
const geoUrl = "/countries.geojson";
const WorldMap = () => {
  return (
    <ComposableMap>
      <Geographies geography={geoUrl}>
        {({ geographies }) =>
          geographies.map((geo) => (
            <Geography
              key={geo.rsmKey}
              geography={geo}
              onMouseEnter={() => {
                const { NAME } = geo.properties;
                console.log(`Hovered over: ${NAME}`);
              }}
              style={{
                default: { fill: "#D6D6DA", outline: "none" },
                hover: { fill: "#F53", outline: "none" },
                pressed: { fill: "#E42", outline: "none" },
              }}
            />
          ))
        }
      </Geographies>
    </ComposableMap>
  );
};

export default WorldMap;

