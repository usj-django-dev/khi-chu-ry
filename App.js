import React from 'react';
// import logo from './logo.svg';
import './App.css';
import Greet from './components/Greet'
import Welcome from './components/welcome'
import Hello from './components/Hello'
function App() {
  return (
    <div className="App">
      <Greet name = "Bruce" heroName="Batman"> 
        <p>This is children props</p> 
      </Greet>

      <Greet name = "Clark" heroName="Superman"> 
        <button>Action</button>
      </Greet>

      {/* <Greet name = "Clark" heroName="Superman"/> */}
      <Greet name = "Diana" heroName="Wounder Womans"/>

      <Welcome name = "Bruce" heroName="Batman"/>
      <Welcome name = "Clark" heroName="Superman"/>
      <Welcome name = "Diana" heroName="Wounder Womans"/>

      {/* <Hello /> */}
    </div>
  );
}

export default App;
