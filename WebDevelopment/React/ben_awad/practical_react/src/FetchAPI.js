import React from "react";
import { useState, useEffect } from "react";

function FetchAPI() {
  const [loading, setLoading] = useState(true);
  const [person, setPerson] = useState(null);

  //https://www.copycat.dev/blog/react-fetch/
  // Note: the empty deps array [] means
  // this useEffect will run once
  // similar to componentDidMount()
  useEffect(() => {
    const url = "https://api.randomuser.me";
    fetch(url)
      .then((res) => res.json())
      .then(
        (result) => {
          setLoading(false);
          setPerson(result.results[0]);
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          setLoading(true);
          //        setError(error);
        }
      );
  }, []);

  return (
    <div>
      {loading || !person ? (
        <div> loading... </div>
      ) : (
        <div>
          <div>
            <div>First Name: {person.name.first}</div>
            <div>Last Name: {person.name.last}</div>
            <div>
              <img src={person.picture.large}></img>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
export default FetchAPI;
