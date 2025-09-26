import './HomeFeedPage.css';
import React from "react";
import { getCurrentUser ,fetchUserAttributes} from '@aws-amplify/auth';
import DesktopNavigation  from '../components/DesktopNavigation';
import DesktopSidebar     from '../components/DesktopSidebar';
import ActivityFeed from '../components/ActivityFeed';
import ActivityForm from '../components/ActivityForm';
import ReplyForm from '../components/ReplyForm';

// [TODO] Authenication
import Cookies from 'js-cookie'

export default function HomeFeedPage() {
  const [activities, setActivities] = React.useState([]);
  const [popped, setPopped] = React.useState(false);
  const [poppedReply, setPoppedReply] = React.useState(false);
  const [replyActivity, setReplyActivity] = React.useState({});
  const [user, setUser] = React.useState(null);
  const dataFetchedRef = React.useRef(false);

  const loadData = async () => {
    try {
      const backend_url = `http://127.0.0.1:8000/api/activities/home`
      const res = await fetch(backend_url, {
        headers:{
          authorization: `Bearer ${localStorage.getItem("access_token")}`
        },
        method: "GET"
      });
      let resJson = await res.json();
      console.log(resJson);
      if (res.status === 200) {
        setActivities(resJson)
      } else {
        console.log(res)
      }
    } catch (err) {
      console.log(err);
    }
  };


    const checkAuth = async () => {
  try {
    // Get the current authenticated user
    const user = await getCurrentUser({ bypassCache: false });
    console.log("Cognito User:", user);

    // Get user attributes (e.g., given_name, preferred_username)
    const attributes = await fetchUserAttributes();
    console.log("User Attributes:", attributes);

    // Safely set the user state
    setUser({
      display_name: attributes.given_name,
      handle: attributes.preferred_username
    });
  } catch (err) {
    console.error("Authentication error:", err);
  }
};

    const getatributes = async() =>{
    const attributes = await fetchUserAttributes();
    return attributes
  }

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
      <div className='content'>
        <ActivityForm  
          popped={popped}
          setPopped={setPopped} 
          setActivities={setActivities} 
        />
        <ReplyForm 
          activity={replyActivity} 
          popped={poppedReply} 
          setPopped={setPoppedReply} 
          setActivities={setActivities} 
          activities={activities} 
        />
        <ActivityFeed 
          title="Home" 
          setReplyActivity={setReplyActivity} 
          setPopped={setPoppedReply} 
          activities={activities} 
        />
      </div>
      <DesktopSidebar user={user} />
    </article>
  );
}