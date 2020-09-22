import lombok.SneakyThrows;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.util.stream.StreamSupport;

public class Reduce  extends Reducer<Text, IntWritable, Text, IntWritable> {

    private static final Integer SOMA_INICIAL_REDUCER = 0;

    @SneakyThrows
    public void reduce(Text key, Iterable<IntWritable> values, Context context) {
        var soma = StreamSupport
            .stream(values.spliterator(), false)
            .map(IntWritable::get)
            .reduce(SOMA_INICIAL_REDUCER, Integer::sum);
        context.write(key, new IntWritable(soma));
    }
}
