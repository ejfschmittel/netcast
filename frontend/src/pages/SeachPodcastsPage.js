import React from 'react'

import {useQuery} from "@apollo/react-hooks"
import podcastQueries from "../graphql/podcasts"

import PodcastList from "../components/podcast-list"
import PodcastFilter from "../components/podcast-filter"

const SeachPodcastsPage = () => {

    const {lodaing, error, data} = useQuery(podcastQueries.ALL_PODCASTS)


    return (
        <main>
            <div className="container">
                <PodcastFilter />
                <PodcastList data={data}/>
            </div>
        </main>
    )
}

export default SeachPodcastsPage