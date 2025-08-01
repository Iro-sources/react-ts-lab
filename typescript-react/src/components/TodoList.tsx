import React from 'react'
import './styles.css'
import { Todo } from '../model';
import SingleTodo from './SingleTodo';

interface Props{
    todos: Todo[];
    setTodos: React.Dispatch<React.SetStateAction<Todo[]>>;
}
const TodoList: React.FC<Props> = ({todos, setTodos}: Props) => {
  return (
    <div className="todos">{
        todos.map(todo =>(
        //<li>{todo.todo}</li>
        <SingleTodo todo={todo}
        key={todo.id}
        todos={todos}
        setTodos={setTodos}
        />
        ))
    }
    </div>
  )
}

export default TodoList;