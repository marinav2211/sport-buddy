import { useBreakpoints } from '@vueuse/core'

export function useMediaQueries() {
  const breakpoints = useBreakpoints({
    sm: 640, // 640px
    md: 768, // 768px
    lg: 1024, // 1024px
    xl: 1280, // 1280px
  })

  // Вместо создания новых реактивных свойств, мы возвращаем computed свойства напрямую
  return {
    isMobile: breakpoints.smaller('md'),
    isDesktop: breakpoints.greaterOrEqual('md'),
  }
}