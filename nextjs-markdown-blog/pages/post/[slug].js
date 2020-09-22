
import matter from 'gray-matter'
import React from 'react'
import ReactMarkdown from 'react-markdown'

export default function PostTemplate({content, data}) {
    const frontmatter = data
    return (
         <div>
         <h2> {frontmatter.title} </h2>
         <ReactMarkdown source={content} />
         </div>
        )
}

PostTemplate.getInitialProps = async (ctx) => {
    const { slug } = ctx.query
    
    const content = await import(`../../content/${slug}.md`)
    
    const data = matter(content.default)
    
    return { ...data }
}
