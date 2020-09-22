

import React from 'react'

export default function Home(props) {
    return (
         <div>
         Hello from Josias Blog
         Category : {props.blogCategory}
         </div>
        )
}


Home.getInitialProps = () => {
    return {
        blogCategory: 'Testing'
    }
}

