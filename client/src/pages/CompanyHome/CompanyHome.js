import React from 'react'
import './CompanyHome.css'
import { Link } from 'react-router-dom'
const CompanyHome = () => {
  return (
    <>
        <Link to="/companyform"><button>Add Job</button></Link>
        <section className='job-list'>
		<h2>Featured Jobs</h2>
		<div class="job">
			<h3>Web Developer</h3>
			<p>XYZ Company</p>
			
		</div>
		<div class="job">
			<h3>Software Engineer</h3>
			<p>ABC Company</p>
			
		</div>
		<div class="job">
			<h3>UX Designer</h3>
			<p>123 Company</p>
			
		</div>
	</section>

    </>
  )
}

export default CompanyHome