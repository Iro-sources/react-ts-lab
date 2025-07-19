import React, { useState } from 'react';
import './App.css';
import InputField from './components/InputFeild';
import { Todo } from './model';


const App: React.FC =() =>{
  //  const [todo, setTodo] = useState<string | number>("");
  const [todo, setTodo] = useState<string>("");
  const [todos, setTodoS] = useState<Todo[]>([]);
 
  const handleAdd = (e: React.FormEvent) => {
    e.preventDefault();

    if(todo){
      setTodoS([...todos, {id: Date.now(), todo: todo, isDone: false}])
      setTodo("");
    }
};

 console.log(todos);
  return (
    <div className="App">
      <span className="heading">Taskify</span>
    <InputField todo={todo} setTodo={setTodo} handleAdd={handleAdd}/>
    
    
    </div>
  );
}

export default App;

/*

//Types of typecript
let name:string = "mohamed";
//making age variable take both string and number, using unions
let age: number | string;
age = 16;
age = "sixteen";

let isStudent:boolean;
let subjects:string[];

//Tupple that takes fast data
let workPerDay:[string, number];
workPerDay = ["monday", 7];

//Creating an object
/* type Person = {
  name: string
  //To make the age optional
  age?: number
} */

/* let person:Person = {
  name: "mack",
}; */

/* let person:Person = {
  name: "mack",
  age: 52,
}; */

//Defining a function
/* function printName(name: string){
  console.log(name);
}
printName("Mohamed"); */

//let printName: Function;
//let printName: (name: string) => void;
//let newFunc: (name: string) => never;

//A function can have different types of return types

//such variable can take any type
//let personName: unknown;
//Extending a type
/* type Fruits = {
  name: string
  items: number
}
type MyList = Fruits &{
  name: string
  item: number
}


interface Student {
  university: string;
  year: number; 
}

interface department extends Student{
  profession: string
}

const csDepartment = {
  university: "Havard",
  year: 2,
  profession: "Computer science"
}
 */
// function that takes a student object:
/* function registerStudent(student:{
  name:string;
  age?:number;
  subjects:string[];
  studentInfo:department

}): string{
    return `Student ${student.name} from ${student.studentInfo.university}, 
    studying ${student.studentInfo.profession}, enrolled in ${student.subjects.length} subjects.`;

}

const studentExample = {
  name: "Mohamed",
  age: 28,
  subjects: ["Parallel programing", "Descreate math", "Algo"],
  studentInfo:{
    university: "MIT",
    year: 2,
    profession: "Engineering"
  }
};

console.log(registerStudent(studentExample)); */
