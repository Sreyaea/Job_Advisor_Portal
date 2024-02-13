import './Navbar.css'
  
  function Navbar() {
    return (
      // <header>
      //   <div className="h-container">
      //       <div>
      //           <a href="#">
      //           <div className="logo-wrap">
      //               <div 
      //               id="logo" 
      //               className='logo' 
      //               alt="Brand logo"
      //               >
      //               Brand
      //               </div>
      //           </div>
      //           </a> 
      //       </div>
      //       <nav>
      //               <ul className="navbar">
      //               <li><a href="#">Products</a></li>
      //               <li><a href="#">Services</a></li>
      //               <li><a href="#">About</a></li>
      //               <li><a href="#">Contact</a></li>
                    
      //               <button className="btn">Log In</button>
      //               <button className="btn">Sign Up</button>
      //               </ul>
      //       </nav>
      //   </div>
      // </header>
      <header>
        <a href="#" class="logo">Logo</a>
        <ul class="navigation">
          <li><a href="#" class="active">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Events</a></li>
          <li><a href="#">Contact</a></li>
          <li><a href="#">Login</a></li>
          <li><a href="#">SignUp</a></li>


        </ul>
      </header>
    );
  }
  
  export default Navbar;