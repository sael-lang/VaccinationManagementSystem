import React, { useState, useEffect } from 'react';
import { Grid, Paper, Typography, List, ListItem, ListItemText } from '@material-ui/core';
import axios from 'axios';
import Topbar from '../../../scenes/global/Topbar'
import Sidebar from "../../../scenes/global/Sidebar";
import endpoint from '../../../apibackend';
const FeedbackView = () => {
  const [feedbackList, setFeedbackList] = useState([]);
  const [isSidebar, setIsSidebar] = useState(true);

  useEffect(() => {
    fetchFeedbackList();
  }, []);

  const fetchFeedbackList = async () => {
    try {
      const response = await axios.get(`${endpoint}saveFeedback`);
      setFeedbackList(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
    <div className="app">
    <Sidebar isSidebar={isSidebar} />
    <main className="content">
    <Topbar setIsSidebar={setIsSidebar} />
    <Grid container justify="center" alignItems="center" style={{ height: '100vh' }}>
      <Grid item xs={6}>
        <Paper elevation={3} style={{ padding: '2rem' }}>
          <Typography variant="h4">Feedback List</Typography>
          {feedbackList.length > 0 ? (
            <List>
              {feedbackList.map((feedback) => (
                <ListItem key={feedback.id}>
                  <ListItemText primary={feedback.Feedback_msg} secondary={`Submitted by: ${feedback.Father_Email}`} />
                </ListItem>
              ))}
            </List>
          ) : (
            <Typography variant="body1">No feedback available.</Typography>
          )}
        </Paper>
      </Grid>
    </Grid>
    </main>
    </div>
    </>
  );
};

export default FeedbackView;
