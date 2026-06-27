import { NavLink } from 'react-router-dom'

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-100 shadow-sm">
      <div className="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
        <NavLink
          to="/"
          className="text-gray-800 font-bold text-xl tracking-tight hover:text-gray-600 transition-colors"
        >
          Lattice Calendar
        </NavLink>
        <NavLink
          to="/login"
          className={({ isActive }) =>
            `px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
              isActive
                ? 'bg-gray-700 text-white'
                : 'text-gray-500 hover:text-gray-800 hover:bg-gray-100'
            }`
          }
        >
          Sign In
        </NavLink>
      </div>
    </nav>
  )
}
