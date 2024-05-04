package uk.gleissner.loomwebflux.movie;

import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;
import uk.gleissner.loomwebflux.controller.LoomWebFluxController;
import uk.gleissner.loomwebflux.movie.domain.Movie;
import uk.gleissner.loomwebflux.movie.repo.MovieRepo;

import java.util.List;
import java.util.Set;
import java.util.UUID;

import static uk.gleissner.loomwebflux.Approaches.LOOM_NETTY;
import static uk.gleissner.loomwebflux.Approaches.LOOM_TOMCAT;
import static uk.gleissner.loomwebflux.Approaches.PLATFORM_TOMCAT;
import static uk.gleissner.loomwebflux.Approaches.WEBFLUX_NETTY;

@RestController
public class MovieController extends LoomWebFluxController {

    private static final String API_PATH = "/movies";
    private final MovieRepo movieRepo;

    MovieController(Environment environment, MovieRepo movieRepo) {
        super(environment);
        this.movieRepo = movieRepo;
    }

    @GetMapping({PLATFORM_TOMCAT + API_PATH, LOOM_TOMCAT + API_PATH, LOOM_NETTY + API_PATH})
    @ResponseBody
    public Set<Movie> findMoviesByDirectorLastName(@RequestParam String directorLastName,
                                                   @RequestParam Integer delayCallDepth,
                                                   @RequestParam Long delayInMillis) throws InterruptedException {
        log("findMoviesByDirectorLastName");
        waitOrFetchEpochMillis(delayCallDepth, delayInMillis);
        return movieRepo.findMoviesByDirector(directorLastName);
    }

    @GetMapping(WEBFLUX_NETTY + API_PATH)
    @ResponseBody
    public Flux<Movie> findMoviesByDirectorLastNameReactive(@RequestParam String directorLastName,
                                                            @RequestParam Integer delayCallDepth,
                                                            @RequestParam Long delayInMillis) {
        log("findMoviesByDirectorLastNameReactive");
        return waitOrFetchEpochMillisReactive(delayCallDepth, delayInMillis)
                .thenMany(Flux.defer(() -> Flux.fromIterable(movieRepo.findMoviesByDirector(directorLastName))));
    }

    @PostMapping({PLATFORM_TOMCAT + API_PATH, LOOM_TOMCAT + API_PATH, LOOM_NETTY + API_PATH})
    public List<Movie> saveMovies(@RequestBody List<Movie> movies,
                                  @RequestParam Integer delayCallDepth,
                                  @RequestParam Long delayInMillis) throws InterruptedException {
        log("saveMovies");
        waitOrFetchEpochMillis(delayCallDepth, delayInMillis);
        return movieRepo.saveAll(movies);
    }

    @PostMapping(WEBFLUX_NETTY + API_PATH)
    public Flux<Movie> saveMoviesReactive(@RequestBody Flux<Movie> movies,
                                          @RequestParam Integer delayCallDepth,
                                          @RequestParam Long delayInMillis) {
        log("saveMoviesReactive");
        return waitOrFetchEpochMillisReactive(delayCallDepth, delayInMillis)
                .flatMapMany(ignore -> movies.flatMap(movie -> Mono.just(movieRepo.save(movie))));
    }

    @DeleteMapping({PLATFORM_TOMCAT + API_PATH + "/{id}", LOOM_TOMCAT + API_PATH + "/{id}", LOOM_NETTY + API_PATH + "/{id}"})
    public void deleteMovieById(@PathVariable UUID id,
                                @RequestParam Integer delayCallDepth,
                                @RequestParam Long delayInMillis) throws InterruptedException {
        log("deleteMoviesById");
        waitOrFetchEpochMillis(delayCallDepth, delayInMillis);
        movieRepo.deleteById(id);
    }

    @DeleteMapping(WEBFLUX_NETTY + API_PATH + "/{id}")
    public Mono<Void> deleteMovieByIdReactive(@PathVariable UUID id,
                                              @RequestParam Integer delayCallDepth,
                                              @RequestParam Long delayInMillis) {
        log("deleteMoviesByIdReactive");
        return waitOrFetchEpochMillisReactive(delayCallDepth, delayInMillis)
                .then(Mono.fromRunnable(() -> movieRepo.deleteById(id)));
    }
}
