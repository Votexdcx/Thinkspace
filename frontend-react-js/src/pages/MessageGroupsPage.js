import './MessageGroupsPage.css';
import React from "react";

import DesktopNavigation  from '../components/DesktopNavigation';
import MessageGroupFeed from '../components/MessageGroupFeed';

// [TODO] Authenication
import Cookies from 'js-cookie'

export default function MessageGroupsPage() {
  const [messageGroups, setMessageGroups] = React.useState([]);
  const [popped, setPopped] = React.useState([]);
  const [user, setUser] = React.useState(null);
  const dataFetchedRef = React.useRef(false);

  const loadData = async () => {
    try {
      const backend_url = 'http://127.0.0.1:8000/api/activities/home/message_groups'
      const res = await fetch(backend_url, {
          headers:{
              authorization: `Bearer ${localStorage.getItem("access_token")}`
            },
        method: "GET"
      });
      let resJson = await res.json();
      if (res.status === 200) {
        console.log("resJson ", resJson)
        console.log("objectvalues ",Object.values(resJson))
        setMessageGroups(Object.values(resJson.data))
      } else {
        console.log(res)
      }
    } catch (err) {
      console.log(err);
    }
  };  

  const checkAuth = async () => {
    console.log('checkAuth')
    // [TODO] Authenication
    if (Cookies.get('user.logged_in')) {
      setUser({
        display_name: Cookies.get('user.name'),
        handle: Cookies.get('user.username')
      })
    }
  };

  React.useEffect(()=>{
    //prevents double call
    if (dataFetchedRef.current) return;
    dataFetchedRef.current = true;

    loadData();
    checkAuth();
  }, [])
  return (
    <article>
      <DesktopNavigation user={user} active={'home'} setPopped={setPopped} />
      <section className='message_groups'>
        <MessageGroupFeed message_groups={messageGroups} />
      </section>
      <div className='content'>
      </div>
    </article>
  );
}