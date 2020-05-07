import React from 'react';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom"


import PodcastDetailPage from "./pages/podcastDetailPage";
import PodcastSearchPage from "./pages/SeachPodcastsPage";
import EpisodeDetailPage from "./pages/episodeDetailPage";

import Header from "./components/header"

import "./scss/main.scss";


const Test = () => (
  <div>
  <h1>Test</h1>

  </div>
)

function App() {
  return (
    <div className="App">
    

      
      
      <Router>
        <Header />
        <Switch>
          <Route path="/" component={Test} exact={true} />
          <Route path="/podcasts/" component={PodcastSearchPage} exact/>
          <Route path="/podcasts/:podcastid/episode/:episodeid" component={EpisodeDetailPage}/>
          <Route path="/podcasts/:podcastid" component={PodcastDetailPage}/>
          
        </Switch>
      </Router>

    </div>
  );
}

export default App;
