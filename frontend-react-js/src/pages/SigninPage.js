import './SigninPage.css';
import React from "react";
import {ReactComponent as Logo} from '../components/svg/logo.svg';
import { Link } from "react-router-dom";
import { signOut, getCurrentUser, signIn, fetchAuthSession } from '@aws-amplify/auth';


// [TODO] Authenication
import Cookies from 'js-cookie'

export default function SigninPage() {

  const [email, setEmail] = React.useState('');
  const [password, setPassword] = React.useState('');
  const [errors, setErrors] = React.useState('');



 const onsubmit = async (event) => {
  event.preventDefault(); // Prevent form from submitting normally
  setErrors(""); // Clear previous errors
 /* try {
    const existingUser = await getCurrentUser();
    if (existingUser) {
      await signOut(); // Sign out before re-signing in
    }
  } catch (e) {
    // No user currently signed in — safe to proceed
  }
  */

  try {
    const user = await signIn({
      username: email, // 'email' variable from state
      password: password,
    });

    // Get token if available and redirect
    const session = await fetchAuthSession();
    const accessToken = session.tokens?.accessToken?.toString();
    if (accessToken) {
      localStorage.setItem("access_token", accessToken);
      window.location.href = "/";
    } else {
      console.warn("Access token not found in user session.");
    }
  } catch (error) {
    console.error("Sign-in error:", error);

    if (error.code === 'UserNotConfirmedException') {
      window.location.href = "/confirm";
      return;
    }

    setErrors(error.message || "An unknown error occurred.");
  }

  return false;
};

  const email_onchange = (event) => {
    setEmail(event.target.value);
  }
  const password_onchange = (event) => {
    setPassword(event.target.value);
  }

  let el_errors;
  if (errors){
    el_errors = <div className='errors'>{errors}</div>;
  }

  return (
    <article className="signin-article">
      <div className='signin-info'>
        <Logo className='logo' />
      </div>
      <div className='signin-wrapper'>
        <form
          className='signin_form'
          onSubmit={onsubmit}
        >
          <h2>Sign into your Cruddur account</h2>
          <div className='fields'>
            <div className='field text_field username'>
              <label>Email</label>
              <input
                type="text"
                value={email}
                onChange={email_onchange}
              />
            </div>
            <div className='field text_field password'>
              <label>Password</label>
              <input
                type="password"
                value={password}
                onChange={password_onchange}
              />
            </div>
          </div>
          {el_errors}
          <div className='submit'>
            <Link to="/forgot" className="forgot-link">Forgot Password?</Link>
            <button type='submit'>Sign In</button>
          </div>

        </form>
        <div className="dont-have-an-account">
          <span>
            Don't have an account?
          </span>
          <Link to="/signup">Sign up!</Link>
        </div>
      </div>

    </article>
  );
}