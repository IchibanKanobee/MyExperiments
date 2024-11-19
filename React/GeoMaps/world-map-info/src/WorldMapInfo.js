import React, { useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import { scaleOrdinal } from "d3-scale";
import { schemeCategory10 } from "d3-scale-chromatic";

const geoUrl = "/countries.geojson";

const WorldMapInfo = () => {
  const [tooltipContent, setTooltipContent] = useState("");
  const [tooltipPosition, setTooltipPosition] = useState({ x: 0, y: 0 });

  // Color scale using d3-scale
  const colorScale = scaleOrdinal(schemeCategory10);

  return (
    <div>
      <ComposableMap
        onMouseMove={(event) => {
          setTooltipPosition({ x: event.pageX + 10, y: event.pageY + 10 });
        }}
      >
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => (
              <Geography
                key={geo.rsmKey}
                geography={geo}
                onMouseEnter={() => {
                  const NAME = geo.properties.ADMIN;
                  setTooltipContent(`Country: ${NAME}`);
                }}
                onMouseLeave={() => {
                  setTooltipContent("");
                }}
                style={{
                  default: {
                     fill: colorScale(geo.properties.ISO_A3), // Use ISO_A3 for unique country colors
                    outline: "none",
                  },
                  hover: { fill: "#F53", outline: "none" },
                  pressed: { fill: "#E42", outline: "none" },
                }}
              />
            ))
          }
        </Geographies>
      </ComposableMap>
      {tooltipContent && (
        <div
          style={{
            position: "absolute",
            top: tooltipPosition.y,
            left: tooltipPosition.x,
            background: "white",
            padding: "5px",
            border: "1px solid #ccc",
            borderRadius: "4px",
            pointerEvents: "none",
            fontSize: "0.85rem",
          }}
        >
          {tooltipContent}
        </div>
      )}
    </div>
  );
};

export default WorldMapInfo;

