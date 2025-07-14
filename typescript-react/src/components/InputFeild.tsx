import React from 'react'
import "./styles.css";
function InputField() {
  return (
  <form className='input'> 
  <input type="input" placeholder = "task" className="input__box"/> 
  <button className="input_submit" type="submit">Go</button>
  </form>
  );
};

export default InputField;