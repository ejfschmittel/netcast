import { gql } from 'apollo-boost';


const RANDOM_PODCAST = gql`
    query{
        randomPodcast{
            id,
            name
        }
    }
`;


// TODO: PAGINATE QUERY AND ADD FILTERS
const ALL_PODCASTS = gql`
    query{
        allPodcasts{
            id,
              name,
            slug,
            description,
        }
    }
`;


const PODCAST = gql`
    query Podcast($id: Int!){
        podcast(id: $id){
            id,
            name,
            slug,
            description,
        }
    }
`;


export default {
    RANDOM_PODCAST,
    ALL_PODCASTS,
    PODCAST
}