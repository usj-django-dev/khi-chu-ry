import React, { Component } from "react";
import './App.css';
import Book from './components/Book';

class App extends Component {
  state = {
    books: [
      { bookName: "1984", writer: "George Orwell" },
      { bookName: "The Da Vinci Code", writer: "Dan Brown" },
      { bookName: "The Alchemist", writer: "Paulo Coelho" },
    ],
    otherProp: "I am from other Prop"
  }

  ChangeBookState = newBookName => {
    this.setState({
      books: [
        { bookName: newBookName, writer: "George Orwell" },
        { bookName: "The Da Vinci Code", writer: "Dan Brown" },
        { bookName: "Metamorfosis", writer: "Franz Kafka" },
      ],

    });
  }


  changeWithInputState = event => {
    this.setState({
      books: [
        { bookName: event.target.value, writer: "George Orwell" },
        { bookName: "The Da Vinci Code", writer: "Dan Brown" },
        { bookName: "Metamorfosis", writer: "Franz Kafka" },
      ],

    });

  }

  render() {
    const style = {
      border: "1px solid red",
      borderRadius: "5px",
      backgroundColor: "black",
      color: "white"
    };
    console.log(this.state)
    return (
      <div className="App">
        <h1 style={style}> Book List</h1>
        <button onClick={() => this.ChangeBookState("Nineteen-Eighty-Four")}>Change State </button>
        <input type="text" onChange={this.changeWithInputState} ></input>
        <Book
          bookName={this.state.books[0].bookName}
          writer={this.state.books[0].writer}
          inputName={this.changeWithInputState} />
        <Book
          bookName={this.state.books[1].bookName}
          writer={this.state.books[1].writer} />
        <Book
          bookName={this.state.books[2].bookName}
          writer={this.state.books[2].writer}
          change={this.ChangeBookState.bind(this, "Nineteen 84")} />
      </div>
    );

  }
}








export default App;
